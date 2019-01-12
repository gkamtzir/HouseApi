from flask_restful import Resource, request, abort
from sqlalchemy.exc import IntegrityError
from models.Property import Property
from models.PropertyAction import PropertyAction
from models.City import City
from models.HeatingType import HeatingType
from models.DoorFrameType import DoorFrameType
from common.Authentication import fetch_token
from common.Enumerations import EnergyCertificateEnum,\
    PropertyTypeEnum, PropertyActionEnum
from models.Shared import db


class AddPropertyResource(Resource):
    def post(self):
        try:
            # Authorize user.
            id, role = fetch_token(request.headers.get("Authorization"))
            if id is not None and not isinstance(id, int):
                abort(401, status="error", message=id)
            if id is None:
                abort(401, status="error",
                      message="You have to log in to access this resource")
            if role == "user":
                abort(401, status="error",
                      message="Only supervisors can use this resource")

            post_data = request.get_json()

            # Checking if size exists.
            size = post_data.get("size")
            if size is None:
                abort(400, status="error", message="size is required")

            # Checking if size is instance of the int class.
            if not isinstance(size, int):
                abort(400, status="error", message="size must be integer")

            # Checking if size is positive.
            if size < 0:
                abort(400, status="error", message="size must be positive")

            # Checking if action exists.
            action = post_data.get("action")
            if action is None:
                abort(400, status="error", message="action is required")

            # Checking if action is instance of the str class.
            if not isinstance(action, str):
                abort(400, status="error", message="action must be string")

            # Checking if action has appropriate value.
            values = [item.name for item in PropertyActionEnum]

            if action not in values:
                abort(400, status="error",
                      message=("action must have one"
                               " of the following values: {}".format(values)))

            # Checking if price exists.
            price = post_data.get("price")
            if price is None:
                abort(400, status="error", message="price is required")

            # Checking if price is instance of the int class.
            if not isinstance(price, int):
                abort(400, status="error", message="price must be integer")

            # Checking if price is positive.
            if price < 0:
                abort(400, status="error", message="price must be positive")

            # Checking if floor exists.
            floor = post_data.get("floor")
            if floor is None:
                abort(400, status="error", message="floor is required")

            # Checking if floor is instance of the int class.
            if not isinstance(floor, int):
                abort(400, status="error", message="floor must be integer")

            # Checking if floor is in the expected range.
            if floor < -1 or floor > 99:
                abort(400, status="error",
                      message="size must be between -1 and 99")

            # Checking if postal_code exists.
            postal_code = post_data.get("postal_code")
            if postal_code is None:
                abort(400, status="error", message="postal_code is required")

            # Checking if postal_code is instance of the str class.
            if not isinstance(postal_code, str):
                abort(400, status="error",
                      message="postal_code must be string")

            # Checking if postal_code has appropriate length.
            if len(postal_code) > 10:
                abort(400, status="error",
                      message=("postal_code must be consists of at most"
                               " 10 characters"))

            # Checking if street_address exists.
            street_address = post_data.get("street_address")
            if street_address is None:
                abort(400, status="error",
                      message="street_address is required")

            # Checking if street_address is instance of the str class.
            if not isinstance(street_address, str):
                abort(400, status="error",
                      message="street_address must be string")

            # Checking if street_address has appropriate length.
            if len(street_address) > 35:
                abort(400, status="error",
                      message=("street_address must be consists of at most"
                               " 35 characters"))

            # Checking if street_number exists.
            street_number = post_data.get("street_number")
            if street_number is not None:
                # Checking if street_number is instance of the int class.
                if not isinstance(street_number, int):
                    abort(400, status="error",
                          message="street_number must be integer")
                # Checking if street_number is positive.
                if street_number < 0:
                    abort(400, status="error",
                          message="street_number must be positive")

            # Checking if property_type exists.
            property_type = post_data.get("property_type")
            if property_type is None:
                abort(400, status="error", message="property_type is required")

            # Checking if property_type is instance of the str class.
            if not isinstance(property_type, str):
                abort(400, status="error",
                      message="property_type must be string")

            # Checking if energy_certificate has appropriate value.
            values = [item.name for item in PropertyTypeEnum]

            if property_type not in values:
                abort(400, status="error",
                      message=("property_type must have one"
                               " of the following values: {}".format(values)))

            # Checking if rooms exists.
            rooms = post_data.get("rooms")
            if rooms is not None:
                # Checking if rooms is instance of the int class.
                if not isinstance(rooms, int):
                    abort(400, status="error", message="rooms must be integer")

                # Checking if rooms is positive.
                if rooms < 0:
                    abort(400, status="error",
                          message="rooms must be positive")

            # Checking if longitude exists.
            longitude = post_data.get("longitude")
            if longitude is None:
                abort(400, status="error", message="longitude is required")

            # Checking if longitude is instance of the float class.
            if not isinstance(longitude, float):
                abort(400, status="error", message="longitude must be float")

            # Checking if latitude exists.
            latitude = post_data.get("latitude")
            if latitude is None:
                abort(400, status="error", message="latitude is required")

            # Checking if latitude is instance of the float class.
            if not isinstance(latitude, float):
                abort(400, status="error", message="latitude must be float")

            # Checking if energy_certificate exists.
            energy_certificate = post_data.get("energy_certificate")
            if energy_certificate is not None:
                # Checking if energy_certificate is instance of the str class.
                if not isinstance(energy_certificate, str):
                    abort(400, status="error",
                          message="energy_certificate must be string")

                # Checking if energy_certificate has appropriate value.
                values = [item.name for item in EnergyCertificateEnum]

                if energy_certificate not in values:
                    abort(400, status="error",
                          message=("energy_certificate must have one"
                                   " of the following values: {}"
                                   .format(values)))

            # Checking if details exists.
            details = post_data.get("details")
            if details is not None:
                # Checking if details is instance of the str class.
                if not isinstance(details, str):
                    abort(400, status="error",
                          message="details must be string")

                # Checking if details has appropriate length.
                if len(details) > 150:
                    abort(400, status="error",
                          message=("details must be consists of at most"
                                   " 150 characters"))

            # Checking if city_id exists.
            city_id = post_data.get("city_id")
            if city_id is None:
                abort(400, status="error", message="city_id is required")

            # Checking if city_id is instance of the int class.
            if not isinstance(city_id, int):
                abort(400, status="error", message="city_id must be integer")

            # Checking if city_id exists in database.
            city = City.query.filter_by(id=city_id).first()
            if city is None:
                abort(400, status="error",
                      message="city_id = {} does not exist"
                      .format(city_id))

            # Checking if heating_type_id exists.
            heating_type_id = post_data.get("heating_type_id")
            if heating_type_id is None:
                abort(400, status="error",
                      message="heating_type_id is required")

            # Checking if heating_type_id is instance of the int class.
            if not isinstance(heating_type_id, int):
                abort(400, status="error",
                      message="heating_type_id must be integer")

            # Checking if heating_type_id exists in database.
            heating_type = HeatingType.query.filter_by(id=heating_type_id)\
                                      .first()
            if heating_type is None:
                abort(400, status="error",
                      message="heating_type = {} does not exist"
                      .format(heating_type_id))

            # Checking if door_frame_id exists.
            door_frame_id = post_data.get("door_frame_id")
            if door_frame_id is None:
                abort(400, status="error", message="door_frame_id is required")

            # Checking if door_frame_iddoor_frame_id is instance of the
            # int class.
            if not isinstance(door_frame_id, int):
                abort(400, status="error",
                      message="door_frame_id must be integer")

            # Checking if door_frame_id exists in database.
            door_frame = DoorFrameType.query.filter_by(id=door_frame_id) \
                                      .first()
            if door_frame is None:
                abort(400, status="error",
                      message="door_frame_id = {} does not exist"
                      .format(door_frame_id))

            # Creating Property instance.
            property = Property(
                floor,
                postal_code,
                street_address,
                street_number,
                property_type,
                size,
                rooms,
                longitude,
                latitude,
                energy_certificate,
                city_id,
                id,
                heating_type_id,
                door_frame_id,
                details)

            # Saving Property instance.
            db.session.add(property)
            db.session.commit()

            # Creating PropertyAction instance.
            property_action = PropertyAction(
                property_id=property.id,
                action=action,
                price=price)

            # Saving PropertyAction instance.
            db.session.add(property_action)
            db.session.commit()

            return {"status": "success",
                    "message": "Property added successfully"}, 200

        except IntegrityError:
            # Rollback changes.
            db.session.rollback()
            abort(400, status="error",
                  message="Unexpected error. Please try again later")
