const request = require("supertest")
const app = require("../src/app")

describe('GET /', () => {
    let server;
    let name = "Silva"

    beforeAll(() => {
        server = app.listen(0)
    })

    afterAll(() => {
        server.close()
    })


    it("should return Hello World!", async () => {
        const res = await request(app).get(`/${name}`);
        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe(`Hello ${name}`);
    });
});