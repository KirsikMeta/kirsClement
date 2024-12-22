from flask import Flask, render_template
from supabase import create_client, Client

app = Flask(__name__)

# Замените эти значения на ваши собственные
url = "https://mhceiasyoevezkxqmtsc.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1oY2VpYXN5b2V2ZXpreHFtdHNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzQ1NTI3MzYsImV4cCI6MjA1MDEyODczNn0.MpnZCoe7ufBXjKMKEatfolrnzUmRsZl9HP8Wx9r6hiE"

supabase: Client = create_client(url, key)

@app.route('/')
def index():
    # Получаем данные из таблицы 'your_table_name'
    data = supabase.table('ClementsJoin').select('real_name,game_name,static').execute()
    return render_template('index.html', data=data.data)

if __name__ == '__main__':
    app.run(debug=False)
