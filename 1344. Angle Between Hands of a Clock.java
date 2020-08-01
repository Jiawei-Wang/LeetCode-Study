// 读题第一想法：时针的位置由两个int共同决定，分针的位置只由第二个int决定
// 获得较小的夹角：获得两个指针分别与0之间的绝对差，如果大的减去小的小于180，则返回此值
// 否则返回小的+360-大的的值
class Solution {
    public double angleClock(int hour, int minutes) {
        // 对于时针：每小时为30度，每分钟为0.5度
        double hourPos = 30 * hour + 0.5 * minutes;
        // 对于分针：每分钟为6度
        double minPos = 6 * minutes;

        if (hourPos > minPos) {
            if (hourPos - minPos <= 180) {
                return hourPos - minPos;
            } else {
                return minPos + 360 - hourPos;
            }
        } else {
            if (minPos - hourPos <= 180) {
                return minPos - hourPos;
            } else {
                return hourPos + 360 - minPos;
            }
        }

    }
}
