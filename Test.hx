import sys.FileSystem;
import haxe.io.BytesInput;
import sys.io.File;
import haxe.io.Bytes;
import haxe.zip.Reader;

using StringTools;

class Test
{
    static function main()
    {
        var zip = File.getBytes("input/test.fla");
        var reader = new Reader(new BytesInput(zip));
        
        // Shit taken from https://github.com/Dot-Stuff/flxanimate/blob/master/flxanimate/FlxAnimate.hx
        var files = [];
        for (list in reader.read())
        {
            // This is literally just Reader.unzip()
            if (list.compressed)
            {
                var s = haxe.io.Bytes.alloc(list.fileSize);
                var c = new haxe.zip.Uncompress(-15);
                var r = c.execute(list.data, 0, s, 0);
                c.close();
                if (!r.done || r.read != list.data.length || r.write != list.fileSize)
                    throw "Invalid compressed data for " + list.fileName;
                list.data = s;
                list.compressed = false;
                list.dataSize = list.fileSize;
            }

            if (!files.contains(list))
                files.push(list);
        }

        FileSystem.createDirectory("haxetestshit");
        for (file in files)
        {
            if (file.fileName.endsWith("/"))
            {
                FileSystem.createDirectory('haxetestshit/${file.fileName}');
                continue;
            }

            try
            {
                //trace(file.data == null);
                File.saveBytes("haxetestshit/" + file.fileName, file.data);
            }
            catch (e)
            {
                trace("FUCK | " + file.fileName + "| " + e);
            }
        }
    }
}