import 'package:http/http.dart' as http;
fetchdata(String url)async{
  http.Response response=await http.get(Uri.parse('http://127.0.0.1:5000/predict? '));
  return response.body;
  
}