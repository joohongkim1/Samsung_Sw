class Node(object):
    def __init__(self, data, link):
        self.data = data
        self.link = link

    def __str__(self):  # 객체의 내부 정보를 문자열로 반환, 디버깅용
        return "data= %s, link= %s" % (self.data, self.link)

    def __repr__(self):  # 객체 현재값을 JSON 형태로 반환. 추후 JSON.parse() 로 복구위한 문자열
        return '{"data":%s, "link":%d}' % (self.data, self.link)


n1 = Node(100, None)
print("n1", n1)
print("n1", n1.data, n1.link)