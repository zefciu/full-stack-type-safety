import React from "react";
import { ApiApi } from "../schema/apis/ApiApi"
import { Author, Book, Publisher } from "../schema/models";

interface BookDisplayProps {
  bookId: number;
}

interface BookDisplayState {
  book: Book | null
  author: Author | null
  publisher: Publisher | null

}

export class BookDisplay extends React.Component<BookDisplayProps, BookDisplayState> {

  constructor(props: BookDisplayProps) {
    super(props);
    this.state = {book: null, author: null, publisher: null};
  }

  componentDidMount(): void {
    this.fetchData();
  }

  private fetchData(): void {
    const api = new ApiApi();
    api.apiBookRetrieve({id: this.props.bookId}
    ).then(
      (book: Book) => {
        this.setState({book: book});
        let author: Promise<Author|null>;
        if (book.author == null) {
          author = Promise.resolve(null)
        } else {
          author = api.apiAuthorRetrieve({id: book.author});
        }
        let publisher: Promise<Publisher> = api.apiPublisherRetrieve({id: book.publisher});
        return Promise.all([author, publisher] as const);
      }
    ).then(
      ([author, publisher]: [Author|null, Publisher]) => {
        this.setState({publisher: publisher});
        this.setState({author: author});
      }
    );
  }

  render(): JSX.Element {
    if (this.state.book == null) {
      return (<div>…</div>);
    } else {
      return <div>
        <div>
        {this.state.author ? this.state.author.firstName : "-" }
        &nbsp;
        {this.state.author ? this.state.author.lastName : "" }
        </div>
        <h1>
        {this.state.book.title}
        </h1>
        <div>
        {this.state.publisher ? this.state.publisher.name : "-"}
        </div>
      </div>
    }
  }
}
