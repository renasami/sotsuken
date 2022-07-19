from .common import CommonModel


def calc_and_get_company():
    models = CommonModel()
    sql = "select * from users.it_company"
    result = models.fetch_all(sql=sql)
    print(result)
