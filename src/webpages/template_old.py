template_content = """<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: sans-serif;
      margin: 20px;
    }
    .container {
      border: 1px solid #ccc;
      padding: 20px;
      margin-bottom: 20px;
      text-align: center; 
    }
    .driver-list {
      display: inline-block;
      margin-right: 15px;
      margin-bottom: 10px; 
    }
    input[type="text"] {
      width: 150px;
      height: 30px;
      border: 1px solid #ccc;
      border-radius: 5px;
      padding: 5px;
      text-align: center;
    }
    .collapsible {
      background-color: #eee;
      color: #444;
      cursor: pointer;
      padding: 18px;
      width: 100%;
      border: none;
      text-align: center;
      outline: none;
      font-size: 15px;
    }
    .content {
      padding: 0 18px;
      display: none; 
      overflow: hidden;
      background-color: #f1f1f1;
    }
  </style>
</head>
<body>

  <h1 style="text-align: center;"></h1>

  <div class="container">
    <h2>Race {{race_no}}</h2>
    <div class="content" style="display: block;"> 
      <div class="driver-list">
        <input type="text" value="{{driver_1}}">
      </div>
      <div class="driver-list">
        <input type="text" value="{{driver_2}}">
      </div>
      <div class="driver-list">
        <input type="text" value="{{driver_3}}">
      </div>
      <br>
      <div class="driver-list">
        <input type="text" value="{{driver_4}}">
      </div>
      <div class="driver-list">
        <input type="text" value="{{driver_5}}">
      </div>
      <br>
      <div class="driver-list">
        <input type="text" value="{{team_1}}">
      </div>
      <div class="driver-list">
        <input type="text" value="{{team_2}}">
      </div>
      <div class="driver-list">
        <input type="text" value="{{two_x_driver}}">
      </div>
    </div>
  </div>

  <script>
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
          content.style.display = "none";
        } else {
          content.style.display = "block";
        }
      });
    }
  </script>

</body>
</html>"""