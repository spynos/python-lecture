import pickle 


def save_herb_list(herb_list):
    ''' list 자료형의 본초 목록을 저장한다 '''
    with open('herb.pickle', 'wb') as f:
        pickle.dump(herb_list, f)


def get_herb_list():
    ''' pickle로 저장된 list 자료형의 본초 목록을 리턴한다 '''
    import os
    if os.path.exists('herb.pickle'):
        with open('herb.pickle', 'rb') as f:
            herb_list = pickle.load(f)
    else:
        herb_list = []
    return herb_list  


def add_herb(name, content):
    ''' 본초를 추가한다 '''
    herb_list = get_herb_list()

    herb = {
      "name": name,
      "content": content
    }
    herb_list.append(herb)
    save_herb_list(herb_list)


def find_herb(herb_list, name):
    ''' 본초 목록에서 본초명으로 내용을 찾아서 리턴한다 '''
    for herb in herb_list:
        if herb['name'] == name:
            return herb


def read_herb(name):
    ''' 본초명에 해당되는 상세내용을 리턴한다 '''
    herb_list = get_herb_list()
    herb = find_herb(herb_list, name)
    return herb


def modify_herb(name, content):
    ''' 본초명에 해당되는 상세내용을 수정한다 '''
    herb_list = get_herb_list()
    herb = find_herb(herb_list, name)
    herb["name"] = name
    herb["content"] = content
    save_herb_list(herb_list)


def remove_herb(name):
    ''' 본초명에 해당되는 항목을 삭제한다 '''
    herb_list = get_herb_list()
    herb = find_herb(herb_list, name)
    herb_list.remove(herb)
    save_herb_list(herb_list)