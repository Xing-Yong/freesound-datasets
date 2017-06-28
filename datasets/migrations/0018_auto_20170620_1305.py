# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-20 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def add_taxonomy_nodes(apps, schema_editor):
    TaxonomyNode = apps.get_model('datasets', 'TaxonomyNode')
    Taxonomy = apps.get_model('datasets', 'Taxonomy')
    all_taxonomies = Taxonomy.objects.all()

    # loop on all taxonomy
    for taxonomy in all_taxonomies:
        # loop for creating instances for each taxonomy node
        for node_id, node in taxonomy.data.items():
            abstract = 'abstract' in node['restrictions']
            omitted = 'omittedTT' in node['restrictions']
            taxonomy_node =  TaxonomyNode.objects.create(node_id=node_id, 
                                          name=node['name'], 
                                          description=node['description'], 
                                          citation_uri=node['citation_uri'], 
                                          abstract=abstract,
                                          omitted=omitted, 
                                          taxonomy=taxonomy)

        # loop for adding parent relations
        all_taxonomy_nodes = taxonomy.taxonomynode_set.all()
        for taxonomy_node in all_taxonomy_nodes:
            if 'parent_ids' in taxonomy.data[taxonomy_node.node_id]:
                for node_id in taxonomy.data[taxonomy_node.node_id]['parent_ids']:
                    parent_node = TaxonomyNode.objects.get(node_id=node_id)
                    taxonomy_node.parents.add(parent_node)


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0017_categorycomment_dataset'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxonomyNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('citation_uri', models.CharField(max_length=100)),
                ('abstract', models.BooleanField(default=False)),
                ('omitted', models.BooleanField(default=False)),
                ('freesound_examples', models.ManyToManyField(related_name='taxonomy_node', to='datasets.Sound')),
                ('parents', models.ManyToManyField(related_name='children', to='datasets.TaxonomyNode')),
                ('taxonomy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datasets.Taxonomy')),
            ],
        ),
        migrations.AlterField(
            model_name='categorycomment',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.RunPython(add_taxonomy_nodes, migrations.RunPython.noop),
    ]
