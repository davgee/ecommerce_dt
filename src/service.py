import os

from flask import Flask, make_response, jsonify, request
from sqlalchemy.orm import Query

from src.models import Cart, Item
from dotenv import load_dotenv
from src.validators import validate_body
from src.settings import COOKIES_MAX_AGE
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()
app = Flask(__name__)


def get_connection_string():
    login = os.getenv('POSTGRES_USERNAME')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    db_name = os.getenv('POSTGRES_DB')

    return f'postgresql://{login}:{password}@{host}:{port}/{db_name}'


@app.route('/item', methods=['POST'])
def item():
    validation = validate_body(request.json)
    if validation['errors']:
        return make_response(jsonify({
            "success": "false",
            "errors": validation['errors']
        }))
    else:
        resp = make_response()
        validated_parameters = validation['validated_params']
    a = get_connection_string()
    engine = create_engine(get_connection_string(), echo=False)
    Session = sessionmaker(bind=engine)

    cart_id = request.cookies.get('cart-ids')

    if not cart_id:
        with Session() as session:
            c1 = Cart()
            session.add(c1)
            session.commit()
            resp.set_cookie('cart-ids', value=str(c1.id),
                            max_age=COOKIES_MAX_AGE)
    else:
        with Session() as session:
            c1 = Query(Cart, session).filter_by(id=cart_id).first()

    with Session() as session:
        name = validated_parameters.get("name", None)
        value = validated_parameters.get("value", None)
        item_to_check = Query(Item, session) \
            .filter_by(external_id=request.json['external_id'],
                       cart_id=str(c1.id)).first()
        if item_to_check:
            item_to_check.name = name
            item_to_check.value = value
        else:
            itm = Item(cart_id=str(c1.id), name=name, value=value,
                       external_id=request.json['external_id'])
            session.add(itm)
        session.commit()
    resp.status_code = 204
    return resp


if __name__ == '__main__':
    app.run()
