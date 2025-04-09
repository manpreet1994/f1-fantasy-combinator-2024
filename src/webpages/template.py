template_content = """<!DOCTYPE html>
<html>
<head>
  <style>
    .container {
      width: 1000px;
      height: 50px;
      display: flex; 
    }
    .race_name{
      background-color: lightgoldenrodyellow; 
      flex: 1;
      display: flex; 
      justify-content: space-around; /* Space drivers evenly */
    }
    .predicted-team {
      background-color: lightblue; 
      flex: 7;
      display: flex; 
      justify-content: space-around; /* Space drivers evenly */
    }
    .two-x-driver {
      background-color: lightgreen; 
      flex: 2;
      display: flex; 
      justify-content: center; /* Center driver name */
    }
  </style>
</head>
<body>

  <div class="container">
    <div class="predicted-team">
      <p>{{driver_1}}</p> 
      <p>{{driver_2}}</p> 
      <p>{{driver_3}}</p> 
      <p>{{driver_4}}</p> 
      <p>{{driver_5}}</p> 
    </div>
    <div class="two-x-driver">
      <p>{{two_x_driver}} (Turbo Driver)</p> 
    </div>
  </div>

</body>
</html>"""