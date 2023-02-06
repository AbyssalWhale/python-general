class TagCloud:
    # __ makes tags private varriable
    def __init__(self) -> None:
        self.__tags = {}

    def add(self, tag):
        localTag = tag.lower()
        self.__tags[localTag] = self.__tags.get(localTag, 0) + 1

    def __getitem__(self, tag):
        localTag = tag.lower()
        return self.__tags.get(localTag, 0)

    # Overriding method len() for this class
    def __len__(self):
        return len(self.__tags) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")

# return implementation in __getitem__ -
print(cloud["PYthon"])
print(cloud["python1"])

# len()
print(len(cloud))

# return all object dictionaries
print(cloud.__dict__)
# to access private varriable
print(cloud._TagCloud__tags)
