object Solution {
  def mostWordsFound(sentences: Array[String]): Int = {
    sentences.map(s => s.count(_ == ' ')).max + 1
  }
}