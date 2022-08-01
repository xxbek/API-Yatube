from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Post, Comment, Follow, Group

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    def validate(self, data):
        author = get_object_or_404(User, username=data['following'].username)
        follow = Follow.objects.filter(user=self.context['request'].user, following=author).exists()

        if author == self.context['request'].user:
            raise serializers.ValidationError('Вы не можете подписаться на себя.')

        if follow:
            raise serializers.ValidationError('Вы уже подписаны на этого автора.')

        return data

    class Meta:
        fields = ['user', 'following']
        read_only_fields = ('id', 'user')
        model = Follow


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title']
        model = Group
