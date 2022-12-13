function getInput(param){
    const result = [];
    const dataArr = [];
    const nameArr = [];
    const nameArrUn = [];
    const idArr = [];
    const idArrUn = [];
    var data = $('#'+param).find(':input');
    test = data;
    for (var i = 0; i < data.length; i++) {
  
      var id = data[i].id;
      var value = data[i].value;
      var name = data[i].name;
      // console.log("?"+value);
      // console.log("name :"+name);
      if (value) {          
        idArr.push(id);
        nameArr.push(name);
        if (data[i].localName == 'select' && data[i].options[data[i].options.selectedIndex].text != '-') {
            dataArr.push(data[i].options[data[i].options.selectedIndex].text);
        }else if (data[i].localName == 'select' && data[i].options[data[i].options.selectedIndex].text == '-') {
          if (name) {
            // console.log("name is "+name);
            idArrUn.push(id);
            nameArrUn.push(name);
          }
            // idArrUn.push(id);
        }else{
          dataArr.push(value);
        }
      }else{
  
        if (name) {
          // console.log("name is "+name);
          idArrUn.push(id);
        }
        // return result
      }
    }
  
    if (nameArrUn.length > 0) {
      result['status'] = false;
      result['id'] = idArrUn;
      result['name'] = nameArrUn;
    }else{
      result['status'] = true;
      result['id'] = idArr;
      result['value'] = dataArr;
      result['name'] = nameArr;
    }
    console.log(result);
    return result
  }
  