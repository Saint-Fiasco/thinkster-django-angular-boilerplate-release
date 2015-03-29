from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    '''
    @cvar UsuarioSerializer: clase que serializa los objetos usuarios
    @type UsuarioSerializer: ModelSerializer
    '''
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'username', 'fecha_creacion', 'fecha_modificacion',
                  'nombre', 'apellido', 'telefono', 'direccion', 'password',
                  'confirm_password',)
        read_only_fields = ('fecha_creacion', 'fecha_modificacion',)

        def create(self, validated_data):
            return Usuario.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance
