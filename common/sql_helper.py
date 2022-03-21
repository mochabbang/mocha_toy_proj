from django.db import connection

class SqlHelper:
    def get_data_list(self, procedure_name, parameters=None):
        # with connection.cursor() as cursor:
        #     try:
        #         cursor.execute(procedure_name, parameters)
        #         row_data = cursor.fetchall()
        #
        #         data_title = [item[0] for item in cursor.description]
        #         data = [dict(zip(data_title, item)) for item in row_data]
        #     except Exception as e:
        #         print(e)
        #     finally:
        #         cursor.close()
        data = None
        with connection.cursor() as cursor:
            try:
                cursor.execute(procedure_name, parameters)
                row_data = cursor.fetchall()

                data_title = [item[0] for item in cursor.description]
                data = [dict(zip(data_title, item)) for item in row_data]
            except Exception as e:
                print(e)
            finally:
                cursor.close()

        return data

