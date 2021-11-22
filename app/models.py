from app import db
from sqlalchemy_serializer import SerializerMixin

""" Many-To-Many relation table example
TABLE1_TABLE2 = db.Table('ManyToMany_table',
                        db.Column('COLUMN1_NAME', db.Integer, db.ForeignKey('TABLE1.FIELD')),
                        db.Column('COLUMN2_NAME', db.Integer, db.ForeignKey('TABLE2.FIELD'))
                        )
"""


class AdditionalTable(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    # field = db.Column(db.Type, parameter=value)


class Entity(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    # field = db.Column(db.Type, parameter=value)

    # One-To-Many relation
    # table_field = db.Column(db.Integer, db.ForeignKey('table_name.FIELD'), nullable=False)
    # additional_enitity = db.relationship('TableObject', backref=db.backref('entities', lazy=True))

    """ EXAPMLE
    additional_id = db.Column(db.Integer, db.ForeignKey('additional_table.id'), nullable=False)
    aditional = db.relationship('AdditionalTable', backref=db.backref('entities', cascade='save-update, merge, delete, delete-orphan'))
    """
