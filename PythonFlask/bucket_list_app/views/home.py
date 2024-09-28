import sys
sys.dont_write_bytecode = True

from flask import Blueprint, render_template, current_app

home = Blueprint("home", __name__, template_folder="templates")

@home.route("/home", methods=("GET", ))
def display_home():
    # パンくずリスト
    breadcrumb_list = [
        ['Home', '/home', True]
    ]
    # やりたいことリスト
    bucket_list = [
        {
            'no': 1,
            'category': 'カテゴリ',
            'bucket_name': 'でも',
            'limit_date': '2024/12/31',
            'status': '進行中'
        }
    ]
    return render_template(
        "home.html",
        breadcrumb_list=breadcrumb_list,
        bucket_list=bucket_list
    )
