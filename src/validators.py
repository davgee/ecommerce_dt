def validate_body(request_body):
    errors = []
    validated_params = {}
    required_params = [('external_id', str)]
    optional_params = [('value', int), ('name', str)]

    if not request_body:
        errors.append(f'{required_params} should be passed in request body.')
        return {"validated_params": validated_params, "errors": errors}

    for req_param in required_params:
        if req_param[0] not in request_body and \
                type(request_body[req_param[0]]) is req_param[1]:
            errors.append(f'{req_param[0]} should be passed in request body.')
        else:
            validated_params[req_param[0]] = request_body[req_param[0]]

    for opt_param in optional_params:
        if opt_param[0] in request_body and \
                type(request_body[opt_param[0]]) is opt_param[1]:
            validated_params[opt_param[0]] = request_body[opt_param[0]]

    return {"validated_params": validated_params, "errors": errors}
