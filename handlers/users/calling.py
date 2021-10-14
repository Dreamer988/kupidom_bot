from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from google_work.google_work import GoogleWork
from loader import dp
from states import MenuState


@dp.message_handler(state=MenuState.Calling)
async def get_menu(message: types.Message, state=FSMContext):
    await message.answer('Эта функция еще в разработке')
    await state.reset_state()
# values = GoogleWork().google_get_values(sheet_id="1qu2vh3Wcp7gl8qFS9XQzR32ExzKc8-eVVC7v8wLlUxI",
#                                         name_list="Лист обзвона квартир",
#                                         start_col="A",
#                                         end_col="AL",
#                                         major_dimension="ROWS"
#                                         )
# old_date = values[1][37]
# call_object = ''
# for row in values[1:]:
#     if new_date > old_date:
#         old_date = new_date
#         call_object = row
#     else:
#         pass
#
# print(call_object)
