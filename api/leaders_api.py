from api import api_bp
from database import get_top_5_leaders

# url dlya polucheniya spiska liderov
@api_bp.route('/leaders/<int:level>', methods=['GET'])
def get_top_5(level: int =0):
    result = get_top_5_leaders(level)
    leaders = []

    # prohodim po kajdomu obyektu v spiske result
    for i in result:
        print(i)
        leaders.append({i.user_fk.name.name: i.score})
    return {'level': level, 'leaders': leaders}