const request = require("supertest")
const app = require("../src/app")

describe('GET /', () => {
    let server;

    beforeAll(() => {
        server = app.listen(0)
    })

    afterAll(async () => {
        await new Promise(resolve => server.close(resolve));
    })

    it("should return Hello World!", async () => {
        const res = await request(app).get("/");
        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe("Hello World!");
    });
});
