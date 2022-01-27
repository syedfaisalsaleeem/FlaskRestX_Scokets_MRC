from marshmallow import Schema, fields
import datetime
from marshmallow.validate import Regexp, Length
from app import ma
from app.rest_apis.user.models import User
from app.rest_apis.utility.index import calculate_age

def provinceserializer(data):
    province_list = ['sindh','punjab','kph','gilgit baltistan']
    value = list(filter(lambda i:i==data.lower(),province_list))
    if len(value) > 0 : return True
    else: return False

def dateofbirthserializer(data):
    try:
        date_of_birth = datetime.datetime.strptime(data, "%Y-%m-%d")
    except:
        return (False,{"date_of_birth":["Date of Birth must follow YYYY-MM-DD foramt !"]})
    
    age = calculate_age(date_of_birth)
    if age <= 16:
        return (False,{"date_of_birth":["age must be greater than 16 !"]})

    return (True,"Success")

class UserRetrieveSerializer(ma.Schema):
        class Meta:
            model = User
            # Fields to expose, add more if needed.
            fields = ("first_name","last_name","cnic","date_of_birth","province")

class UserSerializer(Schema):
    """ /user [POST]
    Parameters:
    - first_name (str)
    - last_name (str)
    - cnic (str)
    - date_of_birth (str)
    - province (str)
    """

    first_name = fields.Str(required=True,validate=[
        Length(max=20),
        Regexp(
            r"^(?![_.\s])(?!.*[_.]{2})[a-z0-9._\s]+(?<![_.\s])$",
            error="Invalid first name"
        )
    ])
    last_name = fields.Str(required=True,validate=[
        Length(max=20),
        Regexp(
            r"^(?![_.\s])(?!.*[_.]{2})[a-z0-9._\s]+(?<![_.\s])$",
            error="Invalid last name"
        )
    ])
    cnic = fields.Str(required=True,validate=[
        Length(max=13),
        Regexp(
            r"^([0-9]{5}-[0-9]{7}-[0-9]$)|([0-9]{13})",
            error="CNIC No must follow the XXXXX-XXXXXXX-X format or XXXXXXXXXXXXX format!"
        )
    ])
    date_of_birth = fields.Str(required=True)
    province = fields.Str(required=True)