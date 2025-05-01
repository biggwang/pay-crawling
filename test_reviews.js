const store = require('app-store-scraper');

//  리뷰를 가져올 앱의 옵션 설정
const options = {
    appId: 'com.kakaopay.payapp.store',
    country: 'kr', // 한국 리뷰를 원하시면 이 줄의 주석을 해제하세요.
    sort: store.sort.RECENT, //: 최신 리뷰 순
    page: 10, // 일단 첫 페이지 리뷰만 가져와 봅니다. (보통 한 페이지에 최대 50~150개 리뷰)
};

console.log(`[${new Date().toISOString()}] 리뷰 가져오기 시작: appId=${options.appId}, country=${options.country || 'us'}, sort=${options.sort}, page=${options.page || 1}`);

store.reviews(options)
    .then((reviews) => {
        // 리뷰 가져오기 성공 시 실행
        console.log(`[${new Date().toISOString()}] 리뷰 가져오기 성공: 총 ${reviews.length}개 리뷰 로드.`);

        if (reviews.length > 0) {
            console.log("\n--- 첫 번째 리뷰 예시 ---");
            const firstReview = reviews[0];
            console.log(`  날짜: ${firstReview.date}`);
            console.log(`  작성자: ${firstReview.user}`);
            console.log(`  평점: ${firstReview.score} / 5`);
            console.log(`  제목: ${firstReview.title}`);
            console.log(`  내용: ${firstReview.text}`);
            console.log("------------------------\n");

            // 더 많은 리뷰를 보려면 reviews 배열을 순회하며 출력
            console.log(reviews); // 전체 리뷰 데이터 확인 시 이 줄의 주석 해제
        } else {
            console.log("지정된 조건에 해당하는 리뷰를 찾을 수 없습니다.");
        }
    })
    .catch((error) => {
        // 오류 발생 시 실행
        console.error(`[${new Date().toISOString()}] 리뷰 가져오기 중 오류 발생:`);
        console.error(error); // 발생한 오류 출력
        // 오류 상세 내용을 보려면 error 객체를 더 자세히 살펴보거나 console.error(error.stack); 등을 사용할 수 있습니다.
        process.exit(1);
    });

console.log(`[${new Date().toISOString()}] 스크립트 실행 요청 완료. 결과 대기 중...`);