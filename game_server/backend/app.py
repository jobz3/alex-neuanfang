from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jobinroy@localhost:5432/alex-neuanfang'
db = SQLAlchemy(app)

# class GameInfo(db.Model):
#     __tablename__ = 'game_info'
#     __table_args__ = {'autoload_with': db.engine}

# class MemoryPairs(db.Model):
#     __tablename__ = 'memory_pairs'
#     __table_args__ = {'autoload_with': db.engine}

with app.app_context():
    game_info_table = db.Table('game_info', db.metadata, autoload_with=db.engine)
    memory_pairs_table = db.Table('memory_pairs', db.metadata, autoload_with=db.engine)

@app.route('/api/memory_game/info', methods=['GET'])
def get_info():
    # rows = GameInfo.query.all()
    # result = [{column.name: getattr(row, column.name) for column in row.__table__.columns} for row in rows]
    # return jsonify(result)
    with db.engine.connect() as conn:
        result = conn.execute(game_info_table.select())
        rows = [dict(row._mapping) for row in result]
    return jsonify(rows)

@app.route('/api/memory_game/pairs', methods=['GET'])
def get_memory_pairs():
    with db.engine.connect() as conn:
        result = conn.execute(memory_pairs_table.select())
        rows = [dict(row._mapping) for row in result]
    return jsonify(rows)