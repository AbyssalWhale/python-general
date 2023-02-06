class TagCloud:
    def __init__(self) -> None:
        self.tags = {}

    def add(self, tag):
        localTag = tag.lower()
        self.tags[localTag] = self.tags.get(localTag, 0) + 1

    def __getitem__(self, tag):
        localTag = tag.lower()
        return self.tags.get(localTag, 0)

    # Overriding method len() for this class
    def __len__(self):
        return len(self.tags) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
print(cloud.tags)

# return implementation in __getitem__ -
print(cloud["PYthon"])
print(cloud["python1"])

# len()
print(len(cloud))
