# Код и ответ успешного создания курьера
code_for_successful_courier_creation = 201
the_body_of_a_successfully_created_courier = {"ok": True}

# Код и ответ на создание курьера с существующим логином
duplicate_courier_creation_code = 409
the_body_of_the_duplicate_courier_creature = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}

# Код и ответ на создание курьера без логина или пароля
courier_creation_code_without_a_required_field = 400
courier_creation_body_without_a_required_field = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

# Код и ответ на авторизацию курьера с существующим логином и паролем
successful_authorization_code = 200
authorization_id_key = "id"

# Код и ответ на авторизацию курьера без логина или пароля
courier_authorization_code_without_required_fields = 400
courier_authorization_body_without_required_fields = {"code": 400, "message":  "Недостаточно данных для входа"}

# Код и ответ на авторизацию курьера с несуществующей парой логин-пароль
authorization_code_for_a_non_existent_user = 404
authorization_body_for_a_non_existent_user = {"code": 404, "message": "Учетная запись не найдена"}

# Код и ответ на создание заказа
order_creation_code = 201
order_track_key = "track"

# Код и ответ на получение списка заказов
successful_get_orders_list_code = 200
orders_key_orders = "orders"
orders_key_pageInfo = "pageInfo"
orders_key_availableStations = "availableStations"
