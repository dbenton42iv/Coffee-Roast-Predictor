from django.db import models

class RoastSession(models.Model):
    session_id = models.AutoField(primary_key=True)  # Unique ID for each roast session
    start_time = models.DateTimeField(auto_now_add=True)  # Time when the roast session started
    end_time = models.DateTimeField(null=True, blank=True)  # Time when the roast session ended
    temperature_profile = models.JSONField()  # Temperature profile data for the roast session

    def __str__(self):
        return f"RoastSession {self.session_id} - Started at {self.start_time}"

class RoastVariableSet(models.Model):
    variable_set_id = models.AutoField(primary_key=True)  # Unique ID for variable set
    roast_session = models.ForeignKey(RoastSession, related_name='variable_sets', on_delete=models.CASCADE)  # Foreign key to RoastSession
    variable_name = models.CharField(max_length=255)  # Name of the variable
    value = models.FloatField()  # Value of the variable

    def __str__(self):
        return f"Variable {self.variable_name} in set {self.variable_set_id}"

class Prediction(models.Model):
    prediction_id = models.AutoField(primary_key=True)  # Unique ID for prediction
    roast_session = models.ForeignKey(RoastSession, related_name='predictions', on_delete=models.CASCADE)  # Foreign key to RoastSession
    predicted_value = models.FloatField()  # Predicted value for this session
    created_at = models.DateTimeField(auto_now_add=True)  # When the prediction was made

    def __str__(self):
        return f"Prediction {self.prediction_id} for session {self.roast_session.session_id}"