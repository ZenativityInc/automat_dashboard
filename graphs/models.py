from django.db import models


class LiquidMasterTable(models.Model):
    index = models.BigIntegerField(primary_key=True)
    electrolyte_id = models.TextField(db_column='Electrolyte ID', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lab_batch = models.IntegerField(blank=True, null=True)
    note = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    total_mass_g_field = models.FloatField(db_column='total_mass(g)', blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    generation_method = models.TextField(blank=True, null=True)
    generation_project = models.TextField(blank=True, null=True)
    conductivity = models.FloatField(db_column='Conductivity', blank=True, null=True)  # Field name made lowercase.
    voltage = models.FloatField(db_column='Voltage', blank=True, null=True)  # Field name made lowercase.
    cycles = models.IntegerField(db_column='Cycles', blank=True, null=True)  # Field name made lowercase.
    lce = models.FloatField(db_column='LCE', blank=True, null=True)  # Field name made lowercase.
    initial_li_efficiency = models.FloatField(db_column='Initial Li efficiency', blank=True,
                                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    generation_id = models.FloatField(blank=True, null=True)
    predicted_conductivity = models.FloatField(db_column='Predicted Conductivity', blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    predicted_voltage = models.FloatField(db_column='Predicted Voltage', blank=True,
                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    predicted_lce = models.FloatField(db_column='Predicted LCE', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Liquid Master Table'
