var React = require('react')
var ReactDOM = require('react-dom')

class Header extends React.Component {
  constructor(props) {
      super(props);
      this.search = this.search.bind(this);
      this.handleKeypress = this.handleKeypress.bind(this);

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
    let urlpattern = this.props.urlpattern
    let school = this.props.school
    let keyword = $('#search-form').val();
    let qrystr = `keyword=${keyword}`
    window.location.href = `${urlpattern}?${qrystr}&school=${school}`
  }
  handleKeypress(event){
    if(event.key == 'Enter'){
      this.search()
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

const Pagination = (props) => {
  let school = props.items.school,
      ctype  = props.items.ctype,
      length = props.items.TotalPage;
  let querystring = (new URL(location)).searchParams;
  let startID = querystring.get('start')
  let start = (querystring.get('start')-1)/10+1
  let end = start + 11 < length ? start + 11 : length
  const turnLeft = (event) => {
    window.location.href = `/infernoWeb/sloth?school=${school}&start=${parseInt(startID)-10}&ctype=${ctype}`
  }
  const turnRight = (event) => {
    window.location.href = `/infernoWeb/sloth?school=${school}&start=${parseInt(startID)+10}&ctype=${ctype}`;

  }
  return(
    <div className="ui grid">
      <div className="three wide column"></div>
      <div className="ui borderless menu">
        <a className="item" id='turnleft' onClick={turnLeft}><i className="angle left icon"></i></a>
        {
          Array.from({length: end-(start-1)}, (v, k) => (k+start-1) ).map((item, index)=>{
            if(item+1==start){
              return <a key={index} className="item active" href={`/infernoWeb/sloth?school=${school}&start=${item*10+1}&ctype=${ctype}`}>{item+1}</a>
            }
            return <a key={index} className="item" href={`/infernoWeb/sloth?school=${school}&start=${item*10+1}&ctype=${ctype}`}>{item+1}</a>
          })
        }
        <a className="item" id='turnright' onClick={turnRight}><i className="angle right icon"></i></a>
      </div>          
    </div>
  )
}

class SideBar extends React.Component{
  render(){
    const sidebarCatelog = ['通識', '必修', '選修', '其他'];
    return(
      <div className="two wide column">
        <div className="ui vertical menu" id="kind">
          {
            sidebarCatelog.map((item, idx) => (
              <a key={idx} className="item" href={"/infernoWeb/sloth?school=nchu&start=1&ctype="+item}>{item}</a>             
            ))
          }
        </div>
      </div>
    );
  }
}

const ContentList = (props) => {
  return(
    <div className="twelve wide mobie eight wide tablet six wide computer column" id="courseList">
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
      pageData:{}
    }
  }
  componentDidMount() {
    $.getJSON(this.props.api, (json) => {
      const first = json.shift()
      var length = first['TotalPage']
      var school = first['school']
      var ctype = first['ctype']

      this.setState({
        items: json,
        pageData: first
      });
    })
  }
  render() {
    return (
      <div className="ui centered grid" id="InfoArea">
        <div className="row">
          <SideBar/>
          <ContentList items={this.state.items}/>              
        </div>
        <div className="row">
          <Pagination items={this.state.pageData}/>
        </div>
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