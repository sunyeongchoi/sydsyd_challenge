## [Error]System limit for number of file watchers reached

- linux에서 기본적으로 inotify를 사용하여 디렉토리 변경 사항을 모니터하는데 모니터링 할 수 있는 파일 수에 대한 시스템 제한이 발생하는 것이라고 한다.

```jsx
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```

- file watchers의 제한을 늘려주는 작업

### React Hook 에러

```jsx
// CreateContents.tsx
const inputResourceTableTitle = localeName('inputresource');
..
<ButtonTable
          title={inputResourceTableTitle}
...
/>
//localeformat.tsx
import {useIntl} from "react-intl";

export const localeName = (bcname: string) => {
    const {formatMessage} = useIntl();
    const kindName = 'w.'+ bcname.toLowerCase();
    return formatMessage({id: kindName});
}
```

- 이렇게 코드 작성시 자꾸 죽어버리는 에러 발생
- 원인 : localeformat.tsx를 보면 useIntl이라는 hook이 사용되었다. 그러나 hook을 전역 변수로 사용하면 안되기 때문에 자꾸 죽었다.
- hook 에서 주의 할 점
  1. 전역변수 사용 금지
  2. 조건문 사용 금지
  3. 두번째 단어 첫 글자의 네이밍 대문자

```jsx
// CreateContents.tsx
const inputResourceTableTitle = () => localeName('inputresource');

<ButtonTable
          title={inputResourceTableTitle()}
...
/>
```

- 이렇게 함수로 고치니 됐다.