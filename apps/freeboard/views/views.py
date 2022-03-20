from django.shortcuts import render
from common.sql_helper import SqlHelper
from common.convert_model import ModelMapper
from apps.freeboard.models.models import Transaction

# Create your views here.
def show_trasaction_list(request):
    sql_helper = SqlHelper()
    model_mapper = ModelMapper()

    data = sql_helper.get_data_list('[dbo].[USP_TransactionHistory_Select_List]')
    list = [model_mapper.make_instance(Transaction(), item) for item in data]

    return render(request, "freeboard/index.html", {
        'transactions': list
    })



# def get_data_list(procedure_name, parameters=None):
#     cursor = connection.cursor()
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
#
#     return data
#
# '''
#     Data To Object
# '''
# def make_instance(instance, values):
#     attributes = instance.__dict__.keys()
#
#     for attribute in attributes:
#         try:
#             # field names from oracle sp are UPPER CASE
#             # we want to put PIC_ID in pic_id etc.
#             # setattr(instance, a, values.get(a))
#             # del values.get(a)
#             if attribute in values.keys():
#                 setattr(instance, attribute, values.get(attribute))
#                 values.pop(attribute)
#         except AttributeError:
#             pass
#         except Exception as e:
#             print(e)
#
#     for other_key in values.keys():
#         setattr(instance, other_key, values.get(other_key))
#
#     return instance

