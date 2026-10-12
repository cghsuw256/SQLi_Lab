from django.db import DatabaseError
from django.shortcuts import render

from .forms import LoginForm
from .models import Auth


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        mode = request.POST.get("mode")

        if form.is_valid() and mode in ["vulnerable", "safe"]:
            account = form.cleaned_data["account"]
            password = form.cleaned_data["password"]
            results = []
            sql_text = ""
            params = []
            error = ""

            try:
                if mode == "vulnerable":
                    # 실습용 취약 코드: 입력값이 SQL 문법에 직접 들어간다.
                    sql_text = (
                        "SELECT * FROM lab_auth "
                        f"WHERE account = '{account}' AND password = '{password}'"
                    )
                    results = Auth.objects.raw(sql_text, params=None)
                else:
                    # 파라미터 바인딩으로 입력값을 SQL 명령이 아닌 데이터로 처리한다.
                    sql_text = (
                        "SELECT * FROM lab_auth "
                        "WHERE account = %s AND password = %s ORDER BY id"
                    )
                    params = [account, password]
                    results = Auth.objects.raw(sql_text, params=params)

                # 여기서 조회해 DB 오류도 결과 화면에 전달한다.
                results = list(results)
            except DatabaseError:
                results = []
                error = "SQL 실행 오류로 데이터를 조회하지 못했습니다."

            return render(request, "lab/result.html", {
                "title": "취약코드검색 결과" if mode == "vulnerable" else "안전코드검색 결과",
                "sql_text": sql_text,
                "params": params,
                "results": results,
                "error": error,
            })
    else:
        form = LoginForm()

    return render(request, "lab/login.html", {"form": form})


def data_view(request):
    users = Auth.objects.order_by("id")
    return render(request, "lab/data.html", {"users": users})
