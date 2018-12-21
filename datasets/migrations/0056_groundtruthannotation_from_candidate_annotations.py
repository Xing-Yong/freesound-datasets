# Generated by Django 2.0.8 on 2018-12-04 15:09

from django.db import migrations, models
import sys


class Migration(migrations.Migration):

    def add_from_candidate_annotations(apps, schema_editor):
        GroundTruthAnnotation = apps.get_model('datasets', 'GroundTruthAnnotation')
        count = 0
        ground_truth_annotations = GroundTruthAnnotation.objects.all().select_related('from_candidate_annotation')
        num_gt_annotations = ground_truth_annotations.count()
        for ground_truth_annotation in ground_truth_annotations:
            ground_truth_annotation.from_candidate_annotations.add(ground_truth_annotation.from_candidate_annotation)
            sys.stdout.write('\rUpdating field %i of %i (%.2f%%)'
                    % (count + 1, num_gt_annotations, 100.0 * (count + 1) / num_gt_annotations))
            sys.stdout.flush()
            count += 1

    dependencies = [
        ('datasets', '0055_vote_from_expert'),
    ]

    operations = [
        migrations.AddField(
            model_name='groundtruthannotation',
            name='from_candidate_annotations',
            field=models.ManyToManyField(related_name='generated_ground_truth_annotations', to='datasets.CandidateAnnotation'),
        ),
        migrations.RunPython(add_from_candidate_annotations, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='groundtruthannotation',
            name='from_candidate_annotation',
        ),

    ]