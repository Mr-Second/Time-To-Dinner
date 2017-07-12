var React = require('react')

export default class Header extends React.Component {
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
            <img src="/static/stufinite/img/logo.svg" alt="LOGO"/>
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