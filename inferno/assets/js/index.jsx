var React = require('react')
var ReactDOM = require('react-dom')

class Header extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
        url:"https://www.facebook.com/v2.9/dialog/oauth?client_id=199021993947051&redirect_uri=http://login.campass.com.tw/fb?redirect_service=" + props.serviceName,
        loginState: '登入'
      }
  }
  componentDidMount() {
    let loginUrl = "http://login.campass.com.tw"
    $.ajax({
      url: loginUrl + '/fb/user',
      dataType: 'json',
      xhrFields: {
        withCredentials: true
      },
      success: (res) => {
        this.setState({
          url: loginUrl + '/fb/logout?redirect_service=www',
          loginState: '登出',
        })
      },
      error: (res) => {
        // User is not logged in
      }
    }); 
  }
  search() {
    $('#courseList').empty();
    urlpattern = props.urlpattern
    school = props.school
    keyword = $('#search-form').val();
    qrystr = `keyword=${keyword}`
    window.location.href = `${urlpattern}?${qrystr}&school=${school}`
  }
  handleKeypress(event){
    if(event.key == 'Enter'){
      search()
    }
  }
  render(){
    return(
      <header className="ui blue inverted stackable container menu">
        <div className="item">
            <img src="static/stufinite/img/logo.svg" alt="LOGO"/>
        </div>
        <a href="http://www.campass.com.tw/" className="item">課表</a>
        <a href="/infernoWeb/sloth?school=nchu&start=1" className="item">心得</a>
        <a href="/infernoWeb/arrogant?start=1" className="item">實習&職缺</a>
        <div className="ui category search item" id="search">
          <div className="ui transparent icon input">
            <input className="prompt" id='search-form' type="text" placeholder="輸入課程名稱、教師、職缺或公司名稱進行搜尋" onKeyUp={this.handleKeypress}/>
                <i className="search link icon" onClick={this.search}></i>
          </div>
        </div>
        <div className="right menu">
          <a className="item" id='fb-login-btn' href={this.state.url}><i className="fa fa-facebook-square" aria-hidden="true"></i>{this.state.loginState}</a>
        </div>
      </header>
    );    
  }
}

const Footer = () => {
  return(
    <footer className="ui blue inverted stackable container segment">
      <span>Copyright © 2016 All rights reserved.</span>
      <a target="_blank" href="https://www.facebook.com/CoursePickingHelper/"><i className="fa fa-facebook-square" aria-hidden="true"></i></a>
    </footer>
  );
}

const ContentList = (props) => {
  return(
    <div>
      {
        props.items.map((item, idx) => (
          <div className="ui cards" key={idx}>
            <div className="card">
              <div className="content">
                <a className="avatar" href="">
                    <img className="right floated mini ui image" src=""/>
                  </a>
                  <a className="avatar" href="">
                    <div className="header shopTitle">{item['fields']['name']}</div>
                  </a>
                  <div className="meta type"></div>
                  <div className="description" id='School_teacher'></div>
              </div>
              <div className="extra content">
                  <span className="right floated">
                    <i className="ui red heart icon"></i>
                    <span id='feedback_amount'></span>
                </span>
              </div>  
            </div>
          </div>
        ))
      }
    </div>
  );
}

class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          items: [],
        }
    }
    componentDidMount() {
      $.getJSON(this.props.api, (json) => {
        var first = json.shift()
        var length = first['TotalPage']
        var school = first['school']
        var ctype = first['ctype']

        this.setState({
          items: json
        });
      })
    }
    render() {
      return (
        <div>
          <ContentList items={this.state.items}/>
        </div>
      );
    }
}
const Layout = (props) => (
  <div>
    <Header service={props.serviceName} school={props.school} urlpattern={props.urlpattern}/>
    <Content api='http://127.0.0.1:8000/sloth/get/clist?school=nchu&start=1'/>
    <Footer/>
  </div>
);



ReactDOM.render(
  <Layout serviceName='course' school='nchu' urlpattern='/infernoWeb/sloth/search'/>,
  document.getElementById('app')
);