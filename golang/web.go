package main
 
import (
	"fmt"
	"html/template"
	"log"
	"net/http"
    "io/ioutil"
    "os"
)


func home(w http.ResponseWriter, r *http.Request) {
    ip := r.RemoteAddr
    data := []byte(ip)
    ioutil.WriteFile("./web.log",data,os.ModeAppend)
    
    r.ParseForm()
	if r.Method == "GET" {
		t, err := template.ParseFiles("./home.html")
		if err != nil {
			fmt.Fprintf(w, "parse template error: %s", err.Error())
			return
		}
		t.Execute(w, nil)
	} 
}
 
func main() {

	http.HandleFunc("/", home)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}

}

