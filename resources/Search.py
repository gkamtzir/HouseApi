from flask_restful import Resource, request, abort
from models.Property import Property,\
    PropertyWithPriceSchema
from models.PropertyAction import PropertyActionSchema

property_with_price_schema = PropertyWithPriceSchema()
property_action_schema = PropertyActionSchema()


class SearchResource(Resource):
    def post(self):
        post_data = request.get_json()

        # Tuple for dynamically storing filters.
        filters = ()

        # Checking if max_size is instance of the int class.
        max_size = post_data.get("max_size")
        if max_size is not None and not isinstance(max_size, int):
            abort(400, status="error", message="max_size must be integer")

        if max_size is not None:
            filters += (Property.size <= max_size, )

        # Checking if min_size is instance of the int class.
        min_size = post_data.get("min_size")
        if max_size is not None and not isinstance(max_size, int):
            abort(400, status="error", message="max_size must be integer")

        if min_size is not None:
            filters += (Property.size >= min_size, )

        # Checking if max_price is instance of the int class.
        max_price = post_data.get("max_price")
        if max_price is not None and not isinstance(max_price, int):
            abort(400, status="error", message="max_price must be integer")

        # Checking if min_price is instance of the int class.
        min_price = post_data.get("min_price")
        if min_price is not None and not isinstance(min_price, int):
            abort(400, status="error", message="min_price must be integer")

        # Checking if max_floor is instance of the int class.
        max_floor = post_data.get("max_floor")
        if max_floor is not None and not isinstance(max_floor, int):
            abort(400, status="error", message="max_floor must be integer")

        if max_floor is not None:
            filters += (Property.floor <= max_floor, )

        # Checking if min_floor is instance of the int class.
        min_floor = post_data.get("min_floor")
        if min_floor is not None and not isinstance(min_floor, int):
            abort(400, status="error", message="min_floor must be integer")

        if min_floor is not None:
            filters += (Property.floor >= min_floor, )

        # Checking if max_rooms is instance of the int class.
        max_rooms = post_data.get("max_rooms")
        if max_rooms is not None and not isinstance(max_rooms, int):
            abort(400, status="error", message="max_rooms must be integer")

        if max_rooms is not None:
            filters += (Property.rooms <= max_rooms, )

        # Checking if min_rooms is instance of the int class.
        min_rooms = post_data.get("min_rooms")
        if min_rooms is not None and not isinstance(min_rooms, int):
            abort(400, status="error", message="min_rooms must be integer")

        if min_rooms is not None:
            filters += (Property.rooms >= min_rooms, )

        # Checking if city is instance of the str class.
        city = post_data.get("city")
        if city is not None and not isinstance(city, str):
            abort(400, status="error", message="city must be string")

        if city is not None:
            filters += (Property.city == city, )

        action = post_data.get("action")

        # Checking if action exists.
        if action is None:
            abort(400, status="error", message="action is required")

        # Checking if action is instance of the str class.
        if action is not None and not isinstance(action, str):
            abort(400, status="error", message="action must be string")

        # Running the actual query
        properties = Property.query.filter(*filters)

        # Iterate over every property and check if action, max and min price
        # requirements are met.
        result_properties = []
        for property in properties:
            for property_action in property.actions:
                property_action = property_action_schema\
                    .dump(property_action).data
                if property_action["action"] == action:
                    # Adding the price to property.
                    property = property_with_price_schema.dump(property).data
                    property["price"] = property_action["price"]

                    if min_price is not None and max_price is not None:
                        if property_action["price"] >= min_price \
                                and property_action["price"] <= max_price:
                            result_properties.append(property)
                    elif min_price is not None:
                        if property_action["price"] >= min_price:
                            result_properties.append(property)
                    elif max_price is not None:
                        if property_action["price"] <= max_price:
                            result_properties.append(property)
                    else:
                        result_properties.append(property)

        return {"status": "success", "data": result_properties}, 200
