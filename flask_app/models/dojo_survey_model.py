from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Student:
    def __init__ (self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # add survey of student to database
    @classmethod
    def add_survey ( cls, data ):
        query = """
            INSERT INTO dojos (name, location, language, comment)
            VALUES ( %(name)s,  %(location)s, %(language)s, %(comment)s )
        """

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result

    # get a single survey info
    @classmethod
    def get_survey ( cls, data ):
        query = """
            SELECT *
            FROM dojos
            WHERE name = %(name)s and comment = %(comment)s
        """

        result = connectToMySQL( DATABASE ).query_db( query, data )
        current_survey = cls ( result[0])
        return current_survey

    # check for requirements of field and "flashes" warning if not met
    @staticmethod
    def validate_survey( new_student_survey):
        is_valid = True
        if len( new_student_survey['name'] ) < 3:
            flash( "You must provide a name. At least 3 letters.", "error_name")
            is_valid = False
        if new_student_survey['location'] == 'none':
            flash( 'Please select a location.', 'error_location')
            is_valid = False
        if new_student_survey['language'] == 'none':
            flash( 'Please select a language.', 'error_language' )
            is_valid = False
        if len( new_student_survey['comment'] ) < 3:
            flash( 'Please leave a comment.', 'error_comment' )
            is_valid = False
        return is_valid
