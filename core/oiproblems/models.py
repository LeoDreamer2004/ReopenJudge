from django.db.models import *


class User(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=100)
    password = CharField(max_length=100)  # This is not secure, but we will fix it later
    email = EmailField()


class Group(Model):
    name = CharField(max_length=100)
    url = URLField()
    logo_id = IntegerField(null=True)  # null means default logo
    description = TextField()
    admin = ForeignKey(User, on_delete=CASCADE, default=1, related_name="admin_of_group")
    # current types:
    # A: college-teaching
    # B: college-competition
    # C: high-school-teaching
    # D: high-school-competition
    # E: interest-group
    group_type = CharField(max_length=1)
    members = ManyToManyField(User)

    @property
    def large_logo_url(self):
        if self.logo_id is not None:
            return f"http://media.openjudge.cn/groups/{self.logo_id}/logo_large.jpg"
        else:
            return "http://static.openjudge.cn/images/default_logo_large.png"

    @property
    def small_logo_url(self):
        if self.logo_id is not None:
            return f"http://media.openjudge.cn/groups/{self.logo_id}/logo_small.jpg"
        else:
            return "http://static.openjudge.cn/images/default_logo_small.png"

    @staticmethod
    def get_logo_id(small_logo_url: str):
        if small_logo_url.endswith("/default_logo_small.png"):
            return None
        return int(small_logo_url.split("/")[-2])


class Announcement(Model):
    publisher = ForeignKey(Group, on_delete=CASCADE)
    content = CharField(max_length=100)
    date = DateTimeField()


class Match(Model):
    name = CharField(max_length=100)
    start_time = DateTimeField()
    end_time = DateTimeField()
    group = ForeignKey(Group, on_delete=CASCADE)


class Problem(Model):
    title = CharField(max_length=100)
    description = TextField()
    difficulty = IntegerField()
    match = ForeignKey(Match, null=True, on_delete=CASCADE)

    def __str__(self):
        return self.title
