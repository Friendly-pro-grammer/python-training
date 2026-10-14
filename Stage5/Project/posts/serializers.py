from rest_framework import serializers
from .models import Tag,Category,Post,Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id","name"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"]
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        source = "author.name",
        read_only = True
    )
    class Meta:
        model = Comment
        fields =[
            "id",
            "author",
            "body",
            "created_at"
        ]
        read_only_fields = ["id", "created_at"]
class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        source="author.name",
        read_only = True
    )
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source = "category",
        write_only = True,
        required=False,
        allow_null =True
    )
    tags = TagSerializer(many=True,read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source="tags",
        many=True,
        write_only=True,
        required=False
    )
    comment_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "author",
            "category",
            "category_id",
            "tags",
            "tag_ids",
            "status",
            "summary",
            "created_at",
            "published_at",
            "comment_count",
        ]
        read_only_fields = [
                "id",
                "author",
                "created_at",
                "published_at",
                "comment_count",
            ]
    def validate_title(self,value):
        if len(value.strip()<5):
            raise serializers.ValidationError("Title must be at least 5 character")
        return value
    def validate(self, attrs):
        instance=getattr(self,"instance",None)
        status =attrs.get(
            "status",
            instance.status if instance else Post.Status.DRAFT
        )
        body =attrs.get(
            "body",
            instance.body if instance else ""
        )
        if status == Post.Status.PUBLISHED and len(body.strip()) < 100:
            raise serializers.ValidationError({
                "body": "Published posts must contain at least 100 characters."
            })

        return attrs

    