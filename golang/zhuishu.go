
// testHtmlLogin project main.go
package main
 
import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
 
//	. "github.com/soekchl/myUtils"
)
 
var (
	change = make(map[string][]byte)
)
 
func init() {
	//loadHtml("login", "login.html")
	loadHtml("home", "home.html")
}
 
func main() {
 
	http.HandleFunc("/", home)
	//http.HandleFunc("/login", Login)
 
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
	//	Error(err)
	}
}
 
 
// 控制各个模块的 log输出开关
func home(w http.ResponseWriter, r *http.Request) {
	user := r.FormValue("user")
	passwd := r.FormValue("passwd")
	//Notice("user=", user, " passwd=", passwd)
	if len(user) == 0 || len(passwd) == 0 {
		fmt.Fprintf(w, "%s", change["home"])
	} else {
		http.Redirect(w, r, "/", htmlReplacer.Replace("www.baidu.com")) // 跳转回主页
	}
	http.Redirect(w, r, "/", htmlReplacer.Replace("www.baidu.com")) // 跳转回主页
}
 
func loadHtml(key, file_name string) {
	info, err := readFile(file_name)
	if err != nil {
	//	Error(err)
		return
	}
	change[key] = info
}
 
func readFile(file_name string) ([]byte, error) {
	fi, err := os.Open(file_name)
	if err != nil {
		panic(err)
	}
	defer fi.Close()
	return ioutil.ReadAll(fi)
}


