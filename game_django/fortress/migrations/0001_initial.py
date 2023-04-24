# Generated by Django 3.2.18 on 2023-04-23 12:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import fortress.models.game_


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectileManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectiles', models.JSONField(default=list)),
                ('last_location', models.JSONField(default=list)),
                ('position', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='StageManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_stage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Projectile',
            fields=[
                ('gameobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fortress.gameobject')),
                ('angle', models.FloatField()),
                ('power', models.FloatField()),
                ('size', models.IntegerField(default=3)),
                ('velocity', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
            bases=('fortress.gameobject',),
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('gameobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fortress.gameobject')),
                ('angle', models.FloatField()),
                ('power', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=('fortress.gameobject',),
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('gameobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fortress.gameobject')),
                ('size', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('fortress.gameobject',),
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('gameobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fortress.gameobject')),
                ('heights', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
            bases=('fortress.gameobject',),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(default=fortress.models.game_.generate_unique_id, max_length=32, unique=True)),
                ('is_game_over', models.BooleanField(default=False, null=True)),
                ('projectile_manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fortress.projectilemanager')),
                ('stage_manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fortress.stagemanager')),
            ],
        ),
        migrations.CreateModel(
            name='StageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('stage_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='fortress.stagemanager')),
                ('tank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fortress.tank')),
                ('target', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fortress.target')),
                ('terrain', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fortress.terrain')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_x', models.IntegerField()),
                ('target_y', models.IntegerField()),
                ('tank_x', models.IntegerField()),
                ('tank_y', models.IntegerField()),
                ('tank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fortress.tank')),
                ('target', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fortress.target')),
                ('terrain', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fortress.terrain')),
            ],
        ),
    ]