// 회원정보 유효성검사
function checkID(id){
    var idRegExp = /^[a-zA-z0-9]{4,12}$/; //아이디 유효성 검사        
    if(id==="" || !idRegExp.test(id))  return false;
    else return true; //확인이 완료되었을 때  
}

function checkPW(password){
    var num = password.search(/[0-9]/g);
    var eng = password.search(/[a-z]/ig);
    var spe = password.search(/[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/gi);

    if(password.length < 8 || password.length > 20){
        return false;
    }else if(password.search(/\s/) != -1){
        return false;
    }else if(num < 0 || eng < 0 || spe < 0 ){
        return false;
    }else {
        return true;
    }

    // var passwordRegExp=/^[a-zA-z0-9]{4,12}$/;//비밀번호 유효성 검사
    // if(password==="" || !passwordRegExp.test(password))
    //     return false;
    // else return true;
}

function checkName(nickname){
    var nicknameRegExp=/[~!@#$%^&*()_+|<>?:{}]/;//닉네임 유효성 검사
    if(nickname===""||nicknameRegExp.test(nickname))
        return false;
    else return true;
}

function checkAddr(address){
    var addressRegExp=/[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;//거주지 유효성 검사
    if(address==="" || !addressRegExp.test(address))
        return false;
    else return true;
}


//회원가입 버튼 클릭 시 작동
function signUp(){
    let id = document.getElementById("id").value
    let password = document.getElementById("password").value
    let nickname = document.getElementById("nickname").value
    let address = document.getElementById("address").value


    if (!checkID(id)) {
        alert('아이디는 영문 대소문자와 숫자 4~12자리로 입력해야합니다!');
        //id포커스
        id.focus();
    // 비밀번호가 4자리 미만이거나 숫자가 아닐때
    } else if (!checkPW(password)) {
        alert('비밀번호는 영문와 숫자, 특수문자를 혼합하여 8~12자리로 입력해야합니다!');
        //비밀번호 포커스
        password.focus();
    } else if (!checkName(nickname)) {
        alert('닉네임에 특수문자를 포함할 수 없습니다.')
        age.focus();
    // 이메일이 입력되지 않았을시
    } else if (!checkAddr(address)) {
        alert('올바른 지역을 입력하세요.');
        email.focus();
    } else {
        location.href = "success.html";
    }
    
    
}