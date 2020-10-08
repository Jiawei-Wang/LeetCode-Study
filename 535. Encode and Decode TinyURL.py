# 保存url
full_tiny = {}
tiny_full = {}

# 所有在url中可能出现的符号
letters = string.ascii_letters + string.digits

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # 其实并不需要设计一个方程把每个长url都通过方程变成特定的短url
        # 只需要随机生成一个短url并把它和长url配对即可
        def short_addr():
            ans = ''
            tmp = ''
            # 短url一共有6位
            for i in range(6):
                tmp = letters[random.randint(0, 10000) % 62]
                ans += tmp
            return ans

        # 如果已经有了就不需要再encode
        if longUrl in full_tiny:
            return "http://tinyurl.com/" + full_tiny[longUrl]
        else:
            # encode一个新的
            suffix = short_addr()
            # 把长短双方都保存起来
            full_tiny[longUrl] = suffix
            tiny_full[suffix] = longUrl

            return "http://tinyurl.com/" + suffix


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # 提取出短url的最后6位
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
