from flask_restful import Resource, reqparse
from ..algorithm import Generator

class Service(Resource):
    def post(self):
        #
        # Parse request (replace with your request)
        #
        parser = reqparse.RequestParser()
        parser.add_argument('test', required=True, help="test cannot be blank!")
        args = parser.parse_args()
        test_arg = args['test']

        #
        # Get file (optional)
        #

        #
        # Here to write your algorithm
        #
        myGenerator = Generator(test_arg)
        result = myGenerator.generate()
        
        return {
            "result": result
        }
