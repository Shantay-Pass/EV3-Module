#!/usr/bin/env python3
from threading import Thread
from flask import Flask, request
from flask_restplus import Resource, Api, fields
from parser import parse_instructions
from io import open
from os.path import isfile

app = Flask(__name__)
api = Api(app)

program = api.model('program', {
    'instructions': fields.List(fields.String, required=True, description='Instructions', example=["mov 50 200", "rot 100 90"])
})

@api.route('/echo')
class Echo(Resource):
    def get(self):
        return {'response': 'echo'}

@api.route('/runprogram')
class RunProgram(Resource):
    @api.doc("Run a program given an instruction set")
    @api.expect(program)
    @api.response(400, 'Malformed request')
    @api.response(409, 'Another program is already running')
    @api.response(200, 'Program transfer complete')
    def post(self):
        if isfile('lock'):
            return {'response': 'error', 'message': 'Another program is already running'}, 409

        print(request.json)

        if not request.json or not "instructions" in request.json:
            return {'response': 'error', 'message': 'No instructions provided'}, 400

        open('lock', 'w').close()
        instructions = request.json["instructions"]
        Thread(target = parse_instructions, args = (instructions, )).start()
        return {'response': 'success'}, 200

@api.route('/terminate')
class Terminate(Resource):
    @api.doc("Terminate the currently running program")
    @api.response(400, "No program is currently running or termination is in progress")
    @api.response(200, "Program termination request success")
    def get(self):
        if isfile('terminate'):
            return {'response': 'error', 'message': 'Termination in progress'}, 400
        if not isfile('lock'):
            return {'response': 'error', 'message': 'No program is currently running'}, 400
        open('terminate', 'w').close()
        return {'response': 'success'}, 200

@api.route('/busy')
class Busy(Resource):
    @api.doc("Check if a program is currently running")
    @api.response(200, 'Status information')
    def get(self):
        return {'response': 'success', 'status': isfile('lock')}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)