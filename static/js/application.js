document.querySelector("#login-form").addEventListener("submit", function (e) {
  if (document.querySelector("#name").value == "") {
    // id 라는 id 를 선택하고 해당 input이 공백일 경우
    e.preventDefault(); // 폼 전송을 막음
    alert("⛔ 이름을 입력해주세요⛔"); // '아이디를 입력해주세요' 라는 경고창을 띄움
  } else if (document.querySelector("#email").value == "") {
    // password 라는 id 를 선택하고 해당 input이 공백일 경우
    e.preventDefault(); // 폼 전송을 막음
    alert("⛔ 메일을 입력해주세요⛔"); // '비밀번호를 입력해주세요' 라는 경고창을 띄움
  } else if (document.querySelector("#github").value == "") {
    // password 라는 id 를 선택하고 해당 input이 공백일 경우
    e.preventDefault(); // 폼 전송을 막음
    alert("⛔ github 주소를 입력해주세요⛔"); // '비밀번호를 입력해주세요' 라는 경고창을 띄움
  } else if (document.querySelector("#str").value == "") {
    // password 라는 id 를 선택하고 해당 input이 공백일 경우
    e.preventDefault(); // 폼 전송을 막음
    alert("⛔ 장점을 입력해주세요⛔"); // '비밀번호를 입력해주세요' 라는 경고창을 띄움
  } else {
    const admit = `    제출 완료🚨
    승인을 기다리세요 ···  `;
    alert(admit);
  }
});
