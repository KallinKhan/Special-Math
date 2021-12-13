from flask import Flask
from flask_restful import Resource, Api


class SpecialMath(Resource):
    @staticmethod
    def get(number):
        try:
            int_number = int(number)
            return SpecialMath.special_math(int_number)
        except ValueError:
            return "There is a problem with the value you entered. Is it not an integer?"
        except Exception as e:
            return "There was an unforeseen error %s." % repr(e)

    @staticmethod
    def special_math(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            n_2 = 0
            n_1 = 1
            for i in range(2, n):
                n_1, n_2 = i + n_1 + n_2, n_1

            return n + n_1 + n_2


def main():
    app = Flask('Special Math')
    api = Api(app)
    api.add_resource(SpecialMath, '/specialmath/<string:number>')
    app.run(port=5000)


if __name__ == '__main__':
    main()
