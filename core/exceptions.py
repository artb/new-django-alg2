from rest_framework.exceptions import APIException

class VotingNotFoundByEmployeeException(APIException):
    status_code = 400
    default_detail = 'Você não possui votações.'


class EmployeeNotFoundQueryParamsException(APIException):
    status_code = 400
    default_detail = 'Funcionário não informado.'

